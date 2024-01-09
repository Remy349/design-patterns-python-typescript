from threading import Lock, Thread

"""Singleton es un patrón de diseño creacional que garantiza
que tan solo exista un objeto de su tipo y proporciona un único
punto de acceso a él para cualquier otro código."""

"""El patrón tiene prácticamente los mismos pros y contras
que las variables globales. Aunque son muy útiles,
rompen la modularidad de tu código."""

"""No se puede utilizar una clase que dependa del Singleton
en otro contexto. Tendrás que llevar también la clase Singleton.
La mayoría de las veces, esta limitación aparece durante
la creación de pruebas de unidad."""

"""Singleton Thread Safe o Singleton con seguridad en los hilos."""


class SingletonMeta(type):
    """This is a thread-safe implementation of Singleton."""

    _instances = {}

    _lock: Lock = Lock()

    """We now have a lock object that will be used to synchronize
    threads during first access to the Singleton."""

    def __call__(self, *args, **kwargs):
        """Possible changes to the value of the `__init__` argument
        do not affect the returned instance."""

        """Now, imagine that the program has just been launched.
        Since there's no Singleton instance yet, multiple threads can
        simultaneously pass the previous conditional and reach
        this point almost at the same time. The first of them will
        acquire lock and will proceed further,
        while the rest will wait here."""

        with self._lock:
            """The first thread to acquire the lock, reaches this conditional,
            goes inside and creates the Singleton instance. Once it leaves the
            lock block, a thread that might have been waiting for the lock
            release may then enter this section. But since the Singleton field
            is already initialized, the thread won't create a new object."""

            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                self._instances[self] = instance

        return self._instances[self]


class Singleton(metaclass=SingletonMeta):
    value: str = ""

    """We'll use this property to prove that our Singleton really works."""

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """Finally, any singleton should define some business logic,
        which can be executed on its instance."""
        pass


def test_singleton(value: str) -> None:
    singleton = Singleton(value)

    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    print(
        "If you see the same value, then singleton was reused (yay!)\n"
        "If you see different values, "
        "then 2 singletons were created (booo!!)\n\n"
        "RESULT:\n"
    )

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))

    process1.start()
    process2.start()
