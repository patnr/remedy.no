"""Demonstration of local plugin."""
import os


def ls_logos():
    dir = os.path.join("docs", "attachments", "logos")
    if os.path.exists(dir):
        return os.listdir(dir)
    return []


def on_config(config):
    config["extra"]["logos"] = ls_logos()


# def on_page_markdown(markdown, page, **kwargs):
#     # path = page.file.src_uri
#     kwargs["config"]["extra"]["logos"] = ls_logos()


# def on_page_markdown(markdown, **kwargs):
#     return markdown.replace("a", "z")
