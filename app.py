
import streamlit as st
import qrcode

# Page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("📱 QR Generator")
    st.write("Create customized QR codes.")
    st.divider()

    st.subheader("About")
    st.write("Convert text and website URLs into QR codes.")

    st.subheader("Features")
    st.write("✅ Text and URL support")
    st.write("✅ Custom colors")
    st.write("✅ Adjustable size")
    st.write("✅ PNG download")

# Main application
st.title("📱 QR Code Generator")
st.caption("Generate your own customized QR codes in seconds.")
st.divider()

# User input
user_data = st.text_input(
    "Enter text or website URL:",
    placeholder="https://example.com"
)

# Customization
st.subheader("🎨 Customize Your QR Code")

qr_color = st.color_picker(
    "Choose QR Code Color", "#000000"
)

bg_color = st.color_picker(
    "Choose Background Color", "#FFFFFF"
)

qr_size = st.slider(
    "QR Code Size",
    min_value=5,
    max_value=20,
    value=10
)

# Generate button
if st.button("Generate QR Code"):

    if not user_data.strip():
        st.warning("Please enter some text or a URL.")

    elif len(user_data) > 2000:
        st.error("Input is too long. Maximum 2000 characters.")

    elif qr_color.upper() == bg_color.upper():
        st.error("Please choose different QR and background colors.")

    else:
        try:
            # Create QR code
            qr = qrcode.QRCode(
                version=None,
                box_size=qr_size,
                border=4
            )

            qr.add_data(user_data)
            qr.make(fit=True)

            # Create image
            qr_image = qr.make_image(
                fill_color=qr_color,
                back_color=bg_color
            ).get_image()

            # Success message
            st.success("QR Code generated successfully!")

            # Display QR code
            st.image(
                qr_image,
                caption="Your QR Code",
                width=250
            )

            # Download QR code
            from io import BytesIO

            buffer = BytesIO()
            qr_image.save(buffer, format="PNG")

            st.download_button(
                label="⬇️ Download QR Code",
                data=buffer.getvalue(),
                file_name="my_qrcode.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Footer
st.divider()
st.caption("Built with Python and Streamlit | QR Code Generator")
