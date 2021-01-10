"""
EVE Online Single Sign-On (SSO) OAuth2 backend
Documentation at https://eveonline-third-party-documentation.readthedocs.io/en/latest/sso/index.html
"""
from social_core.backends.oauth import BaseOAuth2
from apps.bg_buysys import eveesi_client


class EVEOnlineOAuth2v2(BaseOAuth2):
    """EVE Online OAuth authentication backend"""
    name = 'eveonlinev2'
    BASE_URL = 'https://login.eveonline.com/oauth'
    AUTHORIZATION_URL = BASE_URL + '/authorize'
    ACCESS_TOKEN_URL = BASE_URL + '/token'
    REDIRECT_STATE = False
    ID_KEY = 'CharacterID'
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('CharacterID', 'id'),
        ('expires_in', 'expires'),
        ('CharacterOwnerHash', 'owner_hash', True),
        ('refresh_token', 'refresh_token', True),
    ]
    USER_FIELDS = ['username', 'email', 'character_id', 'corporation_id', 'alliance_id']

    def get_user_details(self, response):
        """Return user details from EVE Online account"""
        user_data = self.user_data(response['access_token'])
        fullname, first_name, last_name = self.get_user_names(
            user_data['CharacterName']
        )
        return {
            'email': '',
            'username': fullname,
            'fullname': fullname,
            'first_name': first_name,
            'last_name': last_name,
            'character_id': user_data['character_id'],
            'corporation_id': user_data['corporation_id'],
            'alliance_id': user_data['alliance_id']
        }

    def user_data(self, access_token, *args, **kwargs):
        """Get Character data from EVE server"""
        results = self.get_json('https://login.eveonline.com/oauth/verify',
                                headers={'Authorization': 'Bearer {0}'.format(access_token)})
        results['corporation_id'] = -1
        results['alliance_id'] = -1

        # Get public character data
        public = eveesi_client.get_character(results['CharacterID'])['data']

        # Add to the results
        results['character_id'] = results['CharacterID']
        if 'corporation_id' in public:
            results['corporation_id'] = public['corporation_id']

        if 'alliance_id' in public:
            results['alliance_id'] = public['alliance_id']

        test = self.setting('USER_FIELDS')

        return results


# Original create_user doesn't honor the 'USER_FIELDS' setting on the backend,
# the backend.setting('USER_FIELD', USER_FIELD) code always produces ''
def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.USER_FIELDS)
    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }
