
def test_local_storage(dashboard):
    print(dashboard._local_storage.get_all_storage())
    print('-----------------------------------------')
    dashboard._local_storage.add_local_storage("Name", "John")
    print('-----------------------------------------')
    print(dashboard._local_storage.get_local_storage("Name"))
