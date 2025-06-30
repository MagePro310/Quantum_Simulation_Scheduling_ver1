from component.sup_sys.backend_loader import load_backends_from_config

config = ConfigLoader()
machines = load_backends_from_config(config.backends)

print(machines.keys())  # Danh sách tên backend đã load
