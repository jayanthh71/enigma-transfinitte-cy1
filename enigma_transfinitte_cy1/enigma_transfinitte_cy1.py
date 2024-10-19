import reflex as rx
from .sidebar import sidebar


class ChatState(rx.State):
    request: str
    response: str
    chat_history: list[tuple[bool, str]] = []
    is_user: bool = True

    def handle_submit(self, data: dict):
        self.request = data["prompt"]
        if not self.request.strip():
            return

        self.chat_history.append((self.is_user, self.request))
        self.get_response()
        self.chat_history.append((not self.is_user, self.response))

    def get_response(self):
        self.response = "waiting"
        # Logic here
        self.response = "This is a test response"

    def clear_history(self):
        self.chat_history = []


def textbubble(is_user: bool, req: str = "", res: str = "") -> rx.Component:
    return rx.flex(
        rx.cond(
            is_user,
            rx.text(
                req,
                padding_inline="10px",
                padding_block="5px",
                background_color="#6e56cf",
                border_radius="12px",
                max_width="70%",
            ),
            rx.cond(
                res == "waiting",
                rx.spinner(),
                rx.text(
                    res,
                    padding_inline="10px",
                    padding_block="5px",
                    background_color="#1f1f1f",
                    border_radius="12px",
                    max_width="70%",
                ),
            ),
        ),
        direction="row-reverse" if is_user else "row",
    )


def chatbox() -> rx.Component:
    return rx.flex(
        rx.scroll_area(
            rx.flex(
                rx.foreach(
                    ChatState.chat_history,
                    lambda chat: rx.cond(
                        chat[0],
                        textbubble(True, req=chat[1]),
                        textbubble(False, res=chat[1]),
                    ),
                ),
                padding="15px",
                direction="column",
                spacing="4",
            ),
            type="hover",
            scrollbars="vertical",
        ),
        rx.hstack(
            rx.form.root(
                rx.input(
                    placeholder="Ask anything",
                    id="prompt",
                    variant="soft",
                    radius="full",
                    height="50px",
                    class_name="relative w-full",
                    padding_inline="15px",
                ),
                on_submit=ChatState.handle_submit,
                reset_on_submit=True,
            ),
            rx.icon_button(
                "trash-2",
                radius="full",
                size="3",
                on_click=ChatState.clear_history,
                disabled=~ChatState.chat_history,
            ),
            align="center",
        ),
        spacing="3",
        direction="column",
        padding="15px",
        border="3px solid #43474e",
        border_radius="12px",
        height="600px",
        width="1100px",
    )


def index() -> rx.Component:
    return rx.container(
        # sidebar(),
        rx.vstack(
            rx.spacer(),
            rx.heading("Welcome to CAST.ai", size="9"),
            rx.divider(),
            chatbox(),
            align="center",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
    )
)
app.add_page(index)
