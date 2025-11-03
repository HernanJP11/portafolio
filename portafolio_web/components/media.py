import reflex as rx
from portafolio_web.components.icon_button import icon_button
from portafolio_web.data import Media
from portafolio_web.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True,
            description="Correo"
            
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv,
                description="Ver Cv"
            ),
            icon_button(
                "github",
                data.github,
                description="Ver Github"
            ),
            icon_button(
                "linkedin",
                data.linkedin,
                description="Ver Linkedin"
            ),
            icon_button(
                "Instagram",
                data.instagram,
                description="Ver Instagram",
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )