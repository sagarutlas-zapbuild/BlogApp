from API.serializers import UserSerializer


def jwt_response_handler(token, user=None, request=None):
    userdata = {}
    print(UserSerializer(user, context={'request': request}).data)
    userdata['id'] = UserSerializer(user, context={'request': request}).data.get('id')
    userdata['email'] = UserSerializer(user, context={'request': request}).data.get('email')
    userdata['name'] = UserSerializer(user, context={'request': request}).data.get('name')
    print(userdata,"\n\n\n")
    return {
        'token': token,
        'user': userdata
    }