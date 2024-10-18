import reflex as rx
from rxconfig import config


class GitHubState(rx.State):
    link: str = ""
    is_link_valid: bool = False

    def validate_link(self) -> None:
        self.is_link_valid = True


class InputState(rx.State):
    input_text: str = ""
    display_language: bool = True
    current_language: str = "None"

    def change_language(self) -> None:
        self.display_language = True


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Code Safety Verification Tool", size="9"),
            rx.divider(),
            rx.text(
                "This tool is used for checking the safety of code snippets with the help of a LLM",
                size="4",
            ),
            rx.hstack(
                rx.input(
                    placeholder="Enter GitHub Repository URL",
                    width="395px",
                    height="35px",
                    value=GitHubState.link,
                    on_change=GitHubState.is_link_valid,
                ),
                rx.button(
                    "Import",
                    width="95px",
                    height="35px",
                    disabled=GitHubState.is_link_valid,
                ),
            ),
            rx.text_area(
                placeholder="Paste code here",
                width="500px",
                height="400px",
            ),
            rx.cond(
                InputState.display_language,
                rx.hstack(
                    rx.badge(
                        InputState.current_language,
                        size="3",
                        width="95px",
                        height="35px",
                    ),
                    rx.button(
                        "Verify",
                        width="95px",
                        height="35px",
                        disabled=bool(InputState.input_text),
                    ),
                ),
            ),
            align="center",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
