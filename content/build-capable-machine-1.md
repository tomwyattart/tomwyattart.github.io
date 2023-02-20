Title: Build Capable Machine Project: I
Date: 2023-02-20 04:39
Category: Project 2: Build Capable Machine

My PC with Ryzen 5 3500U, integrated graphics, and 200GB of usable space does not allow it to work effectively on large datasets. I'd love to be able to run and play with AIs such as [gpt-neox](https://github.com/EleutherAI/gpt-neox) and [stable-diffusion](https://github.com/CompVis/stable-diffusion). The project aims to find cheap, used, capable hardware, buy it and build my incredible "supercomputer" capable of working with big data smoothly.

Following [How To Run GPT-NeoX-20B(GPT3) YouTube guide](https://www.youtube.com/watch?v=bAY85Om5O6A),
running GPT Neox 20B pre-trained models requires ~45GB VRAM, which requires a machine with at least two graphics cards with at least 24GB VRAM. I've found used [Tesla K80S cards on AliExpress](https://www.aliexpress.us/item/3256803271302953.html?spm=a2g0o.productlist.main.21.3d72b1c97C0xQg&pdp_ext_f=%7B%22sku_id%22%3A%2212000025875743144%22%7D&pdp_npi=3%40dis%21USD%21315.0%21315.0%21%21%21%21%21%40212244c416768690851713287d070d%2112000025875743144%21sea%21US%212788674031&curPageLogUid=g3nCZwYauYbz) for ~300$ each. Nothing cheaper with so much VRAM, unfortunately. 

Now I am looking for a capable used motherboard, but for now, I've found people complaining about the issues with the visibility and stability of these cards on consumer motherboards. Articles I've found:

* [superuser: Adding Nvidia Tesla K80 to a consumer motherboard (x399)](https://superuser.com/questions/1629080/adding-nvidia-tesla-k80-to-a-consumer-motherboard-x399)

* [quora: Is there a motherboard that can handle 2 to 8 Nvidia Tesla cards?](https://www.quora.com/Is-there-a-motherboard-that-can-handle-2-to-8-Nvidia-Tesla-cards)

* [medium: A Tesla K80 and Ubuntu in a Consumer Motherboard](https://sjgf.medium.com/a-tesla-k80-and-ubuntu-in-a-consumer-motherboard-ab0edbf0e0d1)

The last article is a successful run. Such a motherboard needs **Re-Size BAR Support**. However, the medium article is only about running 1 Tesla.

Can you suggest using a relatively cheap motherboard to run these two cards? Or should we try some utterly different configuration? I appreciate any feedback greatly. You can publish it on this Reddit topic or open a PR to this [Open Sourced blog](https://github.com/tomwyattart/tomwyattart.github.io) on my GitHub account. At last, you can [buy me a coffee](https://www.buymeacoffee.com/tomwyatt) :) 

