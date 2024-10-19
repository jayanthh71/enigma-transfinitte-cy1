import reflex as rx
from rxconfig import config


class ChatState(rx.State):
    request: str
    response: str

    chat_history: list

    def handle_request(self, data: dict):
        self.request = data["prompt"]
        self.response = "This is a test response"


def textbubble(res_type: str) -> rx.Component:
    return rx.flex(
        rx.cond(
            res_type == "user",
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
                padding_inline="10px",
                padding_block="5px",
                background_color="#482c6c",
                border_radius="12px",
                max_width="70%",
            ),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
                padding_inline="10px",
                padding_block="5px",
                background_color="#1f1f1f",
                border_radius="12px",
                max_width="70%",
            ),
        ),
        direction="row-reverse" if res_type == "user" else "row",
    )


def chatbox() -> rx.Component:
    return rx.flex(
        rx.scroll_area(
            rx.flex(
                textbubble("user"),
                textbubble("ai"),
                textbubble("user"),
                textbubble("ai"),
                padding="15px",
                direction="column",
                spacing="4",
            ),
            type="hover",
            scrollbars="vertical",
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    placeholder="Ask anything",
                    id="prompt",
                    radius="full",
                    height="50px",
                    class_name="relative w-full",
                    padding_inline="15px",
                ),
                rx.icon_button(
                    "arrow-up",
                    radius="full",
                    size="3",
                    background_color="#482c6c",
                ),
                align="center",
            ),
            on_submit=ChatState.handle_request,
            reset_on_submit=True,
        ),
        spacing="3",
        direction="column",
        padding="15px",
        border="1px solid #43474e",
        border_radius="12px",
        height="600px",
        width="1100px",
    )


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.spacer(),
            rx.heading("Code Safety Verification Chatbot", size="9"),
            rx.divider(),
            rx.text(
                "This Chatbot is used for checking the safety of code snippets with the help of a LLM",
                size="4",
            ),
            chatbox(),
            align="center",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
