from factories.modern_factories import ModernFactory
from factories.victorian_factory import VictoriaFactory

victorian_factory = VictoriaFactory()
print(victorian_factory.create_sofa())
print(victorian_factory.create_chair())
print(victorian_factory.create_table())

modern_factory = ModernFactory()
print(modern_factory.create_sofa())
print(modern_factory.create_chair())
print(modern_factory.create_table())