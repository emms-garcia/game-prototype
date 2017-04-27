import pygame


class CustomEvents:
    WARP_EVENT_ID = pygame.USEREVENT + 1


class EventHandler(object):

    @staticmethod
    def post_event(event_id, **kwargs):
        available_events = [
            getattr(CustomEvents, x)
            for x in dir(CustomEvents) if not x.startswith('__')
        ]

        if event_id not in available_events:
            raise RuntimeError(
                'Event {} is not implemented.'.format(event_id)
            )

        # Post the event to the pygame event queue
        pygame.event.post(pygame.event.Event(event_id, **kwargs))
