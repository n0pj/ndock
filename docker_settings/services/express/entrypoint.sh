#!/bin/bash
set -eu

# 一時的なグループを作成
groupadd -g 11111 tmpgrp

# nodeユーザを一時的なグループに一旦所属させる
usermod -g tmpgrp node

# もともと所属していたnodeグループを削除
groupdel node

# ホストユーザのGIDと同じGIDでnode グループを作成
groupadd -g $USER_ID node

# nodeユーザのGID をホストユーザのGIDに設定
usermod -g $USER_ID node

# nodeユーザのUSER_ID をホストユーザのUSER_IDに設定
# usermod -g $LOCALUSER_ID node

# 一時的に作ったグループを削除
groupdel tmpgrp

su node
exec "$@"