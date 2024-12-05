from plyer import notification

notification.notify(
    title="Powiadomienie",
    message="Witam, to moje powiadomienie...",
    timeout=10,
    app_icon = None,
    toast = False
)
