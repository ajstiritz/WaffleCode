import asyncio
import os
import yagmail

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.services.vision import *
from viam.components.camera import Camera


async def connect():
    opts = RobotClient.Options.with_api_key(
      api_key='<YOUR API KEY>',
      api_key_id='<YOUR API KEY ID>'
    )
    return await RobotClient.at_address('<YOUR MACHINE ADDRESS>', opts)


async def main():
    machine = await connect()
    WaffleClassifier = VisionClient.from_robot(machine, "WaffleClassifier")

    while True:
        classifications = await WaffleClassifier.get_classifications_from_camera("StaresatToasterthe3rd", 3)

        found = False
        for d in classifications:
            if d.confidence > 0.35 and d.class_name.lower() == "wafflesup":
                print("Waffles are done")
                found = True

    # TODO: Add in texting code once camera bug is fixed whiterabbit.obj

    await asyncio.sleep(5)
    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())
