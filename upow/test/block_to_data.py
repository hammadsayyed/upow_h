from icecream import ic

from upow.manager import split_block_content

print = ic
def block_to_data(block_content):
    previous_hash, address, merkle_tree, content_time, content_difficulty, random = (
        split_block_content(block_content)
    )
    print(previous_hash, address, merkle_tree, content_time, content_difficulty, random)

block_to_data('0294e143019691e6499fe91e2a7004d9fad8dd0eafdb3694b95e2cc7240caa4c422bb509be7f3559e59a2b520ab4fba91fc424a08455cf891d802f65ffd7e4d28809e13d126aaa6b672683b1f333a8f8ec96e32bd2ca5a14803415faab85fb80486922e37f667200905c8d11')
block_to_data('027240caa4c4245f7c6bb1e4da570cdfc13d73bdbc98f641606ad1837b1924a57e2a2313d70189dc356c292840e2cc0a25e358f3ef929c5d6ff71cc1a88840602e1f4dbb22dec2e37219b92c61434b0a50648084de159f45d8a989dc5469399a5aeb6de37f6671004ee8fbf2')