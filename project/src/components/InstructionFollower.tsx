import { Button } from "./ui/button"
const InstructionFollower = () => {
  return (
    <div className="border border-white rounded-md p-4">
      <div className="grid grid-cols-2 gap-5">
        <div id="Recording" className="grid col-span-1 gap-5 bg-custom_1 p-4 rounded-md">
         <div className="flex flex-col gap-5">
         <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">Speak your prompt</h3>
         <Button><p className="text-center">START RECORDING</p></Button>
         <Button><p className="text-center">STOP RECORDING</p></Button>
         </div>
         <div className="flex flex-col gap-5">
          <Button><p className="text-center">GENERATE IMAGE PROMPT</p></Button>
          <Button><p className="text-center">GENERATE IMAGE</p></Button>
         </div>
        </div>
        <div id="Generated Image" className="grid col-span-1 gap-5 bg-custom_1 p-4 rounded-md">
         <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">Generated Image</h3>
        </div>
      </div>
      <div className="bg-custom_1 p-4 rounded-md my-5 ">
      <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight mb-4 text-center">Generate Story from Image</h3>
      <Button className="w-full"><p className="text-lg">Generate Story</p></Button>
      </div>
    </div>
  )
}

export default InstructionFollower