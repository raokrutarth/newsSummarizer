
class Settings:

    @property
    def app_name(self):
        return "derive"

    @property
    def app_version(self):
        return "v0.1"

    @property
    def cockroachdb_url(self):
        return ""

    @property
    def execution_mode(self):
        return "development"
