from comment.api.comments import ApiComment
from comment.api import vote_url


class VoteApi(ApiComment):
    def login(self, login_data):
        self.login_data = login_data
        return self.add_token(vote_url.LOGIN_URL, login_data)

    def subject(self):
        return self.get_api(vote_url.SUBJECT_URL)

    def teacher(self, teacher_params):
        return self.get_api(vote_url.TEACHER_URL, teacher_params)

    def praise(self, praise_params):
        return self.get_api(vote_url.PRAISE_URL, praise_params)

    def logout(self, logout_data):
        res = self.post_api(vote_url.LOGOUT_URL, logout_data)
        self.login(self.login_data)
        return res



