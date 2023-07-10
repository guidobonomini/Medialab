from factory.django import DjangoModelFactory


class PollFactory(DjangoModelFactory):
    vote = Faker("vote")
    category = Faker("category")
