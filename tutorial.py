import streamlit as st
from styles import MAIN_STYLES, CUSTOM_BUTTON_STYLES, get_callout

# Initialize session state for tutorial progress and completion
if "tutorial_step" not in st.session_state:
    st.session_state.tutorial_step = 1
if "tutorial_complete" not in st.session_state:
    st.session_state.tutorial_complete = False

def show_ddm_tutorial():
    """Interactive DDM tutorial walkthrough"""
    st.markdown(MAIN_STYLES, unsafe_allow_html=True)
    st.markdown(CUSTOM_BUTTON_STYLES, unsafe_allow_html=True)

    # Only show the expander if tutorial isn't marked as complete
    if not st.session_state.tutorial_complete:
        with st.expander("🎓 Interactive Tutorial (Start Here)", expanded=True):
            st.markdown("## Dividend Discount Model Tutorial\nLearn how to value stocks using dividend discount models")

            # Step 1: DDM Basics
            if st.session_state.tutorial_step == 1:
                st.markdown("""
                **Step 1/5: Understanding DDM Basics**
                
                Key Concepts:
                - Stock value = Present value of all future dividends
                - Three main variants:
                  1. Zero-Growth Model
                  2. Gordon Growth Model
                  3. Multi-Stage DDM
                - Required return > Growth rate for valid results
                """)

                col1, col2 = st.columns([3, 2])
                with col1:
                    st.latex(r"P = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}")
                with col2:
                    st.markdown(get_callout("Example Dividend", "$2.00", "dividend"), unsafe_allow_html=True)
                    st.markdown(get_callout("Example Return", "10%", "return"), unsafe_allow_html=True)

                if st.button("Next ➡️", key="tut_step1"):
                    st.session_state.tutorial_step = 2

            # Step 2: Zero-Growth Model
            elif st.session_state.tutorial_step == 2:
                st.markdown("**Zero-Growth Model: Step 2/5**")
                st.latex(r"P = \frac{D}{r}")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(get_callout("Dividend (D)", "$2.00/year", "dividend"), unsafe_allow_html=True)
                    st.markdown(get_callout("Required Return (r)", "10%", "return"), unsafe_allow_html=True)
                    st.latex(r"P = \frac{2.00}{0.10} = 20.00")

                with col2:
                    st.markdown(get_callout("When to Use", "<ul><li>Utility companies</li><li>REITs</li><li>Mature blue chips</li></ul>", "usage"), unsafe_allow_html=True)

                if st.button("⬅️ Previous", key="tut_step2_prev"):
                    st.session_state.tutorial_step = 1
                if st.button("Next ➡️ Gordon Growth Model", key="tut_step2"):
                    st.session_state.tutorial_step = 3

            # Step 3: Gordon Growth Model
            elif st.session_state.tutorial_step == 3:
                st.markdown("**Gordon Growth Model: Step 3/5**")
                st.latex(r"P = \frac{D_1}{r - g}")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(get_callout("D₀", "$2.00", "dividend"), unsafe_allow_html=True)
                    st.markdown(get_callout("Growth (g)", "5%", "growth"), unsafe_allow_html=True)
                    st.markdown(get_callout("Return (r)", "10%", "return"), unsafe_allow_html=True)
                    st.latex(r"""
                    \begin{aligned}
                    D_1 &= 2.00 \times (1 + 0.05) = 2.10 \\
                    P &= \frac{2.10}{0.10 - 0.05} = 42.00
                    \end{aligned}
                    """)

                with col2:
                    st.markdown(get_callout("Best For", "<ul><li>Consumer staples</li><li>Dividend aristocrats</li><li>Stable growth firms</li></ul>", "usage"), unsafe_allow_html=True)

                if st.button("⬅️ Previous", key="tut_step3_prev"):
                    st.session_state.tutorial_step = 2
                if st.button("Next ➡️ Multi-Stage DDM", key="tut_step3"):
                    st.session_state.tutorial_step = 4

            # Step 4: Multi-Stage DDM
            elif st.session_state.tutorial_step == 4:
                st.markdown("**Multi-Stage DDM: Step 4/5**")
                st.latex(r"P = \sum_{t=1}^n \frac{D_0(1+g_i)^t}{(1+r)^t} + \frac{D_n(1+g_s)}{(r-g_s)(1+r)^n}")

                if st.button("⬅️ Previous", key="tut_step4_prev"):
                    st.session_state.tutorial_step = 3
                if st.button("Next ➡️ Practical Application", key="tut_step4"):
                    st.session_state.tutorial_step = 5

            # Step 5: Practical Application (Completion)
            elif st.session_state.tutorial_step == 5:
                st.markdown(get_callout("Using the DDM App", """
                <ol>
                    <li>Enter stock ticker for historical data</li>
                    <li>Select valuation model</li>
                    <li>Adjust inputs using number fields</li>
                    <li>Review valuation results</li>
                    <li>Explore sensitivity plots</li>
                </ol>
                """, "neutral"), unsafe_allow_html=True)

                st.markdown(get_callout("Best Practices", """
                <ul>
                    <li>Compare multiple models</li>
                    <li>Validate growth assumptions</li>
                    <li>Use historical data as reference</li>
                    <li>Consider market conditions</li>
                </ul>
                """, "best-practice"), unsafe_allow_html=True)

                if st.button("⬅️ Previous", key="tut_step5_prev"):
                    st.session_state.tutorial_step = 4
                if st.button("✅ Finish Tutorial", key="tut_step5"):
                    st.session_state.tutorial_complete = True

    # Step 5 callouts persist after tutorial collapse
    if st.session_state.tutorial_complete:
        st.markdown(get_callout("Using the DDM App", """
        <ol>
            <li>Enter stock ticker for historical data</li>
            <li>Select valuation model</li>
            <li>Adjust inputs using number fields</li>
            <li>Review valuation results</li>
            <li>Explore sensitivity plots</li>
        </ol>
        """, "neutral"), unsafe_allow_html=True)

        st.markdown(get_callout("Best Practices", """
        <ul>
            <li>Compare multiple models</li>
            <li>Validate growth assumptions</li>
            <li>Use historical data as reference</li>
            <li>Consider market conditions</li>
        </ul>
        """, "best-practice"), unsafe_allow_html=True)
