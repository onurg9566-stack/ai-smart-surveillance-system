# =====================================================
# NOTIFICATION SYSTEM (TELEGRAM / LOG)
# =====================================================
#
# Amaç:
# Sistem uyarılarını bildirmek
#
# Şimdilik console log yapıyoruz
# (istersen Telegram ekleriz)
#
# =====================================================

class Notifier:

    def __init__(self):

        print("Notifier hazır.")

    def send_alert(self, message):

        # gerçek projede Telegram API olur
        print(f"[ALERT NOTIFICATION] {message}")
