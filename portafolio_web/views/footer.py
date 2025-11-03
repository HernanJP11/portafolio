import reflex as rx
from portafolio_web.components.media import media
from portafolio_web.data import Media
from portafolio_web.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Contacto"),
        media(data),
        spacing=Size.SMALL.value
    )