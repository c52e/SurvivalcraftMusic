# SurvivalcraftMusic

将简谱转化为生存战争音乐播放器的格式

## 使用说明

* 生存战争中音乐播放器共有4个八度加上额外的一个do（49种频率），程序中可识别的简谱共有7个八度，在确保最高音和最低音只差不超过48个半音的情况下，可以通过调整transToSurvivalCraft函数shift的值，将频率整体移动到生存战争中的有效范围
* transToSurvivalCraft函数的turn_num的值用于奇偶交替
* 运行ChiisanaKoiNoUta.py或canon.py或secret_base.py示例以获取详细信息
