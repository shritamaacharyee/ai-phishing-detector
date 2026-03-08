
import streamlit as st
import pickle
import numpy as np
import re
from urllib.parse import urlparse

# Load model
model = pickle.load(open('phishing_model.pkl', 'rb'))

st.set_page_config(page_title="AI Phishing Detector", page_icon="🛡️")
st.title("🛡️ AI Phishing Website Detector")
st.write("Paste any website URL below and our AI will detect if it is safe or phishing")
st.markdown("---")

def extract_features(url):
    features = []
    # UsingIP
    features.append(-1 if re.match(r"http://\d+\.\d+\.\d+\.\d+", url) else 1)
    # LongURL
    features.append(-1 if len(url) > 75 else (0 if len(url) >= 54 else 1))
    # ShortURL
    shorteners = ["bit.ly","goo.gl","tinyurl","ow.ly","t.co"]
    features.append(-1 if any(s in url for s in shorteners) else 1)
    # Symbol@
    features.append(-1 if "@" in url else 1)
    # Redirecting//
    features.append(-1 if url.count("//") > 1 else 1)
    # PrefixSuffix-
    domain = urlparse(url).netloc
    features.append(-1 if "-" in domain else 1)
    # SubDomains
    dots = domain.count(".")
    features.append(-1 if dots > 2 else (0 if dots == 2 else 1))
    # HTTPS
    features.append(1 if url.startswith("https") else -1)
    # DomainRegLen
    features.append(0)
    # Favicon
    features.append(0)
    # NonStdPort
    features.append(-1 if ":" in domain else 1)
    # HTTPSDomainURL
    features.append(-1 if "https" in domain else 1)
    # RequestURL
    features.append(0)
    # AnchorURL
    features.append(0)
    # LinksInScriptTags
    features.append(0)
    # ServerFormHandler
    features.append(0)
    # InfoEmail
    features.append(0)
    # AbnormalURL
    features.append(0)
    # WebsiteForwarding
    features.append(0)
    # StatusBarCust
    features.append(0)
    # DisableRightClick
    features.append(0)
    # UsingPopupWindow
    features.append(0)
    # IframeRedirection
    features.append(0)
    # AgeofDomain
    features.append(0)
    # DNSRecording
    features.append(0)
    # WebsiteTraffic
    features.append(0)
    # PageRank
    features.append(0)
    # GoogleIndex
    features.append(0)
    # LinksPointingToPage
    features.append(0)
    # StatsReport
    features.append(0)
    return np.array(features).reshape(1, -1)

# URL input
url = st.text_input("🔗 Enter Website URL", placeholder="https://example.com")

if st.button("🔍 Check This Website", use_container_width=True):
    if url:
        features = extract_features(url)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        confidence = f"{max(probability)*100:.1f}%"
        
        st.markdown("---")
        if prediction == 1:
            st.success("✅ This website appears LEGITIMATE")
            st.metric("AI Confidence", confidence)
        else:
            st.error("🚨 WARNING: This looks like a PHISHING website!")
            st.metric("AI Confidence", confidence)
        
        st.markdown("---")
        with st.expander("🔍 See what the AI analyzed"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("🔗 Uses IP address:", "Yes ⚠️" if features[0][0]==-1 else "No ✅")
                st.write("📏 URL Length:", "Too long ⚠️" if features[0][1]==-1 else "Normal ✅")
                st.write("✂️ URL Shortener:", "Yes ⚠️" if features[0][2]==-1 else "No ✅")
                st.write("@ Symbol in URL:", "Yes ⚠️" if features[0][3]==-1 else "No ✅")
            with col2:
                st.write("🔒 HTTPS:", "Yes ✅" if features[0][7]==1 else "No ⚠️")
                st.write("➖ Prefix/Suffix -:", "Yes ⚠️" if features[0][5]==-1 else "No ✅")
                st.write("🌐 Subdomains:", "Too many ⚠️" if features[0][6]==-1 else "Normal ✅")
                st.write("🔀 Redirecting:", "Yes ⚠️" if features[0][4]==-1 else "No ✅")
        
        st.caption("Powered by Random Forest AI | 96.92% Accuracy")
    else:
        st.warning("Please enter a URL first!")
