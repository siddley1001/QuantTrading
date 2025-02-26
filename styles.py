# styles.py

MAIN_STYLES = """
<style>
    :root {
        /* Primary Colors */
        --color-dividend: #1e88e5;
        --color-return: #43a047;
        --color-growth: #fb8c00;
        --color-initial-growth: #e53935;
        --color-usage: #8e24aa;
        --color-best-practice: #00acc1;
        --color-neutral: #757575;
        
        /* Text Colors */
        --color-text-primary: #212529;
        --color-text-secondary: #495057;
    }

    /* Base Callout Style */
    .ddm-callout {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .ddm-callout h4 {
        color: inherit;
        margin: 0 0 0.5rem 0;
        font-size: 1.1rem;
        font-weight: 600;
    }

    .ddm-callout p {
        margin: 0;
        color: var(--color-text-primary);
        font-size: 1rem;
        line-height: 1.5;
    }

    .ddm-callout ul {
        margin: 0.5rem 0 0 0;
        padding-left: 1.5rem;
    }

    .ddm-callout li {
        margin-bottom: 0.25rem;
    }

    /* Color Variants */
    .ddm-dividend {
        border-color: var(--color-dividend);
        color: var(--color-dividend);
    }

    .ddm-return {
        border-color: var(--color-return);
        color: var(--color-return);
    }

    .ddm-growth {
        border-color: var(--color-growth);
        color: var(--color-growth);
    }

    .ddm-initial-growth {
        border-color: var(--color-initial-growth);
        color: var(--color-initial-growth);
    }

    .ddm-usage {
        border-color: var(--color-usage);
        color: var(--color-usage);
    }

    .ddm-best-practice {
        border-color: var(--color-best-practice);
        color: var(--color-best-practice);
    }

    .ddm-neutral {
        border-color: var(--color-neutral);
        color: var(--color-neutral);
    }
</style>
"""

CUSTOM_BUTTON_STYLES = """
<style>
    /* Primary Button */
    .stButton>button:first-child {
        background-color: var(--color-dividend);
        border-color: var(--color-dividend);
        color: white;
    }

    /* Secondary Button */
    .stButton>button:first-child:disabled {
        background-color: #ffffff;
        color: var(--color-text-primary);
        border-color: #dee2e6;
    }

    /* Hover Effects */
    .stButton>button:first-child:hover {
        opacity: 0.9;
        color: white !important;
    }
</style>
"""

def get_callout(title, content, variant="dividend"):
    """Generate a styled callout box with specified variant"""
    return f"""
    <div class="ddm-callout ddm-{variant}">
        <h4>{title}</h4>
        <div>{content}</div>
    </div>
    """