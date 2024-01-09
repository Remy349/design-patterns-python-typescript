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

"""Singleton Naive o Singleton ingenuo."""


class SingletonMeta(type):
    """The Singleton class can be implemented in different ways in Python.
    Some possible methods include: base class, decorator, metaclass.
    We will use the metaclass because it is best suited for this purpose."""

    _instances = {}

    def __call__(self, *args, **kwargs):
        """Possible changes to the value of the `__init__` argument
        do not affect the returned instance."""

        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance

        return self._instances[self]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """Finally, any singleton should define some business logic,
        which can be executed on its instance."""
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
