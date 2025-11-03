import reflex as rx

from portafolio_web.components.heading import heading
from portafolio_web.components.info_detail import info_detail
from portafolio_web.data import Info
from portafolio_web.styles.styles import Size


def info(title: str, info: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in info
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )