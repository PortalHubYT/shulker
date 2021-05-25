import unittest

from mc_api.components.NBT import NBT
from mc_api.components.Block import Block

class TestBlock(unittest.TestCase):

    def test_NBT_without_args(self):
        tags = NBT()

        diff = repr(tags)
        test = '{}'
        self.assertEqual(diff, test)

    def test_NBT_without_attrs(self):
        b = Block('dirt')

        diff = repr(b.nbt)
        test = '{}'
        self.assertEqual(diff, test)

    def test_NBT_without_args_passed_to_Block(self):
        tags = NBT()
        b = Block('dirt', nbt=tags)

        diff = repr(b.nbt)
        test = '{}'
        self.assertEqual(diff, test)

    def test_NBT_without_args_attributed_to_Block(self):
        tags = NBT()
        b = Block('dirt')

        b.nbt = tags

        diff = repr(b.nbt)
        test = '{}'
        self.assertEqual(diff, test)

    def test_NBT_with_arg(self):
        tags = NBT({"Lock": "45"})

        diff = repr(tags)
        test = '{Lock:"45"}'
        self.assertEqual(diff, test)

    def test_NBT_with_args(self):
        tags = NBT({
                    'Fire': 4,
                    'Air': 10,
                    'AbsorptionAmount': 150.0,
                    'Motion': [2.0 , 2.0 , 2.0], 
                    'Passengers': [ {'id' : "minecraft:area_effect_cloud" } ],
                    'CustomName': '{"text":"test"}'
                    })

        diff = repr(tags)
        test = '{AbsorptionAmount:150.0d,Air:10,CustomName:\'{"text":"test"}\',Fire:4,Motion:[2.0, 2.0, 2.0],Passengers:[{\'id\': \'minecraft:area_effect_cloud\'}]}'
        self.assertEqual(diff, test)

    def test_NBT_via_attr(self):
        tags = NBT()
        tags.fire = 4

        diff = repr(tags)
        test = '{Fire:4}'
        self.assertEqual(diff, test)

    def test_NBT_via_attrs(self):
        tags = NBT()
        tags.motion = [2.0, 2.0, 2.0]
        tags.passengers = [{'id': 'minecraft:area_effect_cloud'}]

        diff = repr(tags)
        test = '{Motion:[2.0, 2.0, 2.0],Passengers:[{\'id\': \'minecraft:area_effect_cloud\'}]}'
        self.assertEqual(diff, test)

    def test_NBT_with_arg_passed_to_Block(self):
        tags = NBT({'Fire': 4})
        b = Block('dirt', nbt=tags)

        diff = repr(b.nbt)
        test = '{Fire:4}'
        self.assertEqual(diff, test)

    def test_NBT_with_args_passed_to_Block(self):
        tags = NBT({
                    'Fire': 4,
                    'Air': 10,
                    'AbsorptionAmount': 150.0,
                    'Motion': [2.0 , 2.0 , 2.0], 
                    'Passengers': [ {'id' : "minecraft:area_effect_cloud" } ],
                    'CustomName': '{"text":"test"}'
                    })
        b = Block('dirt', nbt=tags)

        diff = repr(b.nbt)
        test = '{AbsorptionAmount:150.0d,Air:10,CustomName:\'{"text":"test"}\',Fire:4,Motion:[2.0, 2.0, 2.0],Passengers:[{\'id\': \'minecraft:area_effect_cloud\'}]}'
        self.assertEqual(diff, test)

    def test_NBT_via_attr_through_Block(self):
        b = Block('dirt')
        b.nbt.fire = 4

        diff = repr(b.nbt)
        test = '{Fire:4}'
        self.assertEqual(diff, test)

    def test_NBT_via_attrs_through_Block(self):
        b = Block('dirt')
        b.nbt.motion = [2.0, 2.0, 2.0]
        b.nbt.passengers = [{'id': 'minecraft:area_effect_cloud'}]

        diff = repr(b.nbt)
        test = '{Motion:[2.0, 2.0, 2.0],Passengers:[{\'id\': \'minecraft:area_effect_cloud\'}]}'
        self.assertEqual(diff, test)

    def test_NBT_mixed_attrs_and_args_through_Block(self):
        tags = NBT({"Fire": 4, "CustomName": '{"text":"test"}'})
        b = Block('dirt')
        b.nbt = tags
        b.nbt.motion = [2.0, 2.0, 2.0]
        b.nbt.passengers = [{'id': 'minecraft:area_effect_cloud'}]

        diff = repr(b.nbt)
        test = '{CustomName:\'{"text":"test"}\',Fire:4,Motion:[2.0, 2.0, 2.0],Passengers:[{\'id\': \'minecraft:area_effect_cloud\'}]}'
        self.assertEqual(diff, test)

    

    