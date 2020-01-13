class PaymentStatus:
    WAITING = 'waiting'
    PREAUTH = 'preauth'
    CONFIRMED = 'confirmed'
    REJECTED = 'rejected'
    REFUNDED = 'refunded'
    ERROR = 'error'
    INPUT = 'input'

    CHOICES = [
        (WAITING, 'Waiting for confirmation'),
        (PREAUTH, 'Pre-authorized'),
        (CONFIRMED, 'Confirmed'),
        (REJECTED, 'Rejected'),
        (REFUNDED, 'Refunded'),
        (ERROR, 'Error'),
        (INPUT, 'Input')]
