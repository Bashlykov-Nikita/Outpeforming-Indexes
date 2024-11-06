import streamlit as st


def note_text(note_message: str):
    st.markdown(
        f"""
    <div class="note-block">
        <strong class="note-text">📌Note:</strong> {note_message}.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <style>
        .note-block {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #062633;
            border-left: 4px solid rgb(0 192 242 / 1);

        }
        .note-text {
            color: rgb(0 192 242 / 1)
        }

    </style>
    """,
        unsafe_allow_html=True,
    )


def attention_text(attention_message: str):
    st.markdown(
        f"""
    <div class="attention-block">
        <strong class="attention-text">🔥Important:</strong> {attention_message}.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <style>
        .attention-block {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #481d00;
            border-left: 4px solid rgb(255 164 33 / 1);
            margin-bottom: 1rem;
        }
        .attention-text {
            color: rgb(255 164 33 / 1)
        }

    </style>
    """,
        unsafe_allow_html=True,
    )


def index_none_text():
    return ""


def portfolio_none_text(selected_portfolio):
    if selected_portfolio == "None":
        st.subheader("About Portfolios:")
        st.write(
            "##### - 📈Maximum Sharpe Ratio - a portfolio that aims for the highest possible returns for a given level of risk."
        )
        note_text(
            "MSR portfolio contains no exposure to unrewarded risk (contains only systematic risc)"
        )
        attention_text(
            "Right now, Magic only works in the main Python app file, not in imported files. See GitHub issue #288 for a discussion of the issues."
        )
        st.write(
            "##### - 🛡️Global Minimum Variance - a portfolio with the smallest possible fluctuations in value."
        )
        st.write(
            "##### - ⚖️Equally Weighted - a portfolio where each stock has the same percentage."
        )
        st.write(
            "##### - 🧩Equal Risk Contribution - a portfolio where each stock contributes equally to the overall portfolio risk."
        )
