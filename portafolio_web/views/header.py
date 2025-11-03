import reflex as rx
from portafolio_web.components.heading import heading
from portafolio_web.components.media import media
from portafolio_web.data import Data
from portafolio_web.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.BIG_2.value,
            border="3px solid",
            border_color="cyan",     
            box_shadow="0 0 10px cyan" # Efecto glow
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit",
            ),
            media(data.media),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )