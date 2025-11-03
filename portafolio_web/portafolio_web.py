"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from portafolio_web.data import data
from portafolio_web.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio_web.views.header import header
from portafolio_web.views.about import about
from portafolio_web.views.tech_stack import tech_stack
from portafolio_web.views.info import info
from portafolio_web.views.footer import footer
from rxconfig import config

DATA = data

def index() -> rx.Component:
        return rx.center(
            rx.vstack(
                header(DATA),
                about(DATA.about),
                rx.divider(),
                tech_stack(DATA.technologies),
                info("Proyectos", DATA.projects),
                info("Formación", DATA.training),
                rx.divider(),
                footer(DATA.media),
                spacing=Size.MEDIUM.value,
                padding_x=EmSize.MEDIUM.value,
                padding_y=EmSize.BIG.value,
                max_width=MAX_WIDTH,
                width="100%"
            )
        )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="cyan",
        radius="full"
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
