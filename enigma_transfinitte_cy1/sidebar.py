import reflex as rx


def sidebar() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon_button("menu", size="2"),
            align="start",
            justify="left",
        ),
        # rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.flex(
                    rx.drawer.close(rx.icon_button("chevron-left"), align="right"),
                    align_items="start",
                    direction="row-reverse",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="2em",
                background_color="#1f1f1f",
            )
        ),
        direction="left",
    )
