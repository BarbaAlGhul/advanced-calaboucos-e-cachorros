import pytest

from input_handlers import EventHandler
import tcod.event as te

event_quit = EventHandler.ev_quit

def test_quit():
    with pytest.raises(SystemExit):
        event_quit(EventHandler, te.Quit)

