from swampdragon.serializers.model_serializer import ModelSerializer


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = 'main.TodoList'
        publish_fields = ('name', 'description')


class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = 'main.TodoItem'
        publish_fields = ('done', 'text')
        update_fields = ('done', )