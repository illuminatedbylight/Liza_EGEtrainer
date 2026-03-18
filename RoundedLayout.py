from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class RoundedLayout(BoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), radius=20, **kwargs):
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.radius = dp(radius)

        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[(self.radius, self.radius)]
            )

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
