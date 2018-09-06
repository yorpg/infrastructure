import os


class AwsMeta(object):
    @classmethod
    def table_name(cls, table_name):
        env_name = os.environ.get(table_name + '_TABLE')
        return env_name or table_name

    @classmethod
    def meta(cls, src_name: str):
        src_name = src_name.upper()

        class Meta:
            table_name = cls.table_name(src_name)

        if Meta.table_name == src_name:  # local
            Meta.host = "http://172.17.0.2:8000"
        else:
            Meta.region = 'us-west-2'
        return Meta
