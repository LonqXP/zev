from zev.config.types import (
    SetupQuestionSelect,
    SetupQuestionSelectOption,
    SetupQuestionText,
)

questions = (
    SetupQuestionText(
        name="GEMINI_API_KEY",
        prompt="Your GEMINI api key:",
        default="",
    ),
    SetupQuestionSelect(
        name="GEMINI_MODEL",
        prompt="Choose which model you would like to default to:",
        options=[
            SetupQuestionSelectOption(
                value="gemini-flash-latest",
                label="gemini-flash-latest",
                description="Low latency, good for summarization, good performance",
            ),
            SetupQuestionSelectOption(
                value="gemini-2.0-flash",
                label="gemini-2.0-flash",
                description="Long context, good performance",
            ),
        ],
    ),
)
