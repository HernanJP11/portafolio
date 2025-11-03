import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False, description: str = '') -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            title= description
        ),
        href=url,
        is_external=True
    )