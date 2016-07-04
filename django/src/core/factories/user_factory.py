import factory
from faker import Factory as FakerFactory

from core.models import User

faker = FakerFactory.create()


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    name = factory.LazyAttribute(lambda x: faker.name())
    username = factory.LazyAttribute(lambda x: faker.user_name())
    password = '123456'
    email = factory.LazyAttribute(lambda x: faker.email())
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=6))
    website = factory.LazyAttribute(lambda x: faker.uri())
    is_active = factory.LazyAttribute(lambda x: faker.pybool())
    country = factory.LazyAttribute(lambda x: faker.country_code())

    # nome = Sequence(lambda n: 'alunoanexo%d' % n)
    # hash = Sequence(lambda n: 'hash_%d' % n)
    # mataluno = SubFactory(AlunoFactory)
    # tamanho = Sequence(int)
    # dataupload = Sequence(lambda n: datetime.date(2000, 1, 1) + datetime.timedelta(days=n))
    # publico = Sequence(int)