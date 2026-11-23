from repository.dao_entity import DAOEntity
from service.services import Services
from interface.gui import UI


def main():
    repository = DAOEntity()
    services = Services(repository)
    ui = UI(services)
    ui.show_principal_menu()


if __name__ == "__main__":
    main()