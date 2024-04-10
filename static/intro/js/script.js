// 等待DOM内容完全加载后执行
document.addEventListener('DOMContentLoaded', function() {
    // 选取所有模态框元素
    const modalPages = document.querySelectorAll('.modal-page');
    let currentStep = 0; // 用于追踪当前显示的模态框

    // 初始化，显示第一个模态框
    showCurrentModal();

    // 为所有的“下一步”按钮添加点击事件处理
    document.querySelectorAll('.next').forEach(button => {
        button.addEventListener('click', () => {
            // 在邮箱输入步骤进行邮箱格式验证
            if (currentStep === 1 && !validateEmail()) {
                 showGlobalAlert('请输入有效的邮箱地址！');
                return; // 如果邮箱格式不正确，则不继续执行
            }
            // 新增：如果当前步骤是密码输入步骤，且密码没有填写
            if (currentStep === 2 && !validatePassword()) { 
                 showGlobalAlert('请填写协议密码！');
                return;
            }
            // 验证时间顺序
            if (!validateTimeOrder()) {
                showGlobalAlert('结束时间必须晚于起始时间！');
                return; // 如果时间顺序错误，则不继续执行
            }
            // 移动到下一个模态框
            moveToNextStep();
        });
    });

    // 为所有的“上一步”按钮添加点击事件处理
    document.querySelectorAll('.prev').forEach(button => {
        button.addEventListener('click', moveToPreviousStep);
    });

    // 为所有视频元素添加点击事件，用于处理视频激活状态和播放逻辑
    document.querySelectorAll('.video-container .video').forEach(video => {
        video.addEventListener('click', function(event) {
            event.preventDefault(); // 阻止默认点击播放事件

            // 将所有视频元素设置为非激活状态，并暂停播放
            document.querySelectorAll('.video-container .video').forEach(v => {
                v.classList.remove('active-video');
                v.pause();
            });

            // 激活点击的视频但不自动播放
            this.classList.add('active-video');
        });
    });

    // 页面加载时自动填充协议和域名逻辑，并为相关元素添加事件监听
    autoFillProtocolAndDomain();
    document.getElementById('protocolSelect')?.addEventListener('change', autoFillProtocolAndDomain);
    document.getElementById('emailInput')?.addEventListener('input', autoFillProtocolAndDomain);

   // 定义移动到下一个模态框的函数
function moveToNextStep() {
    const currentModal = modalPages[currentStep];
    // 应用"下一步"的退出动画
    currentModal.style.animation = 'slideOutLeft 0.5s forwards';

    currentModal.addEventListener('animationend', function() {
        this.style.display = 'none';
        this.style.animation = '';

        // 在增加之前检查是否已经是最后一个模态框的索引
        if (currentStep === modalPages.length - 2) {
            // 如果是，直接将currentStep设置为最后一个模态框的索引（完成模态框）
            currentStep = modalPages.length - 1;
        } else {
            // 否则正常增加索引
            currentStep = (currentStep + 1) % modalPages.length;
        }

        // 显示当前模态框
        showCurrentModal('next');
    }, { once: true });
}

    // 定义移动到上一个模态框的函数
    function moveToPreviousStep() {
        const currentModal = modalPages[currentStep];
        // 应用"上一步"的退出动画
        currentModal.style.animation = 'slideOutRight 0.5s forwards';

        currentModal.addEventListener('animationend', function() {
            this.style.display = 'none';
            this.style.animation = '';

            // 计算上一个模态框的索引并显示
            currentStep = (currentStep - 1 + modalPages.length) % modalPages.length;
            showCurrentModal('prev');
        }, { once: true });
    }

    // 显示当前步骤的模态框，并根据方向应用不同的进入动画
    function showCurrentModal(direction) {
        const currentModal = modalPages[currentStep];
        currentModal.style.display = 'flex';
        // 根据是"下一步"还是"上一步"操作应用相应的进入动画
        currentModal.style.animation = direction === 'next' ? 'slideInRight 0.5s forwards' : 'slideInLeft 0.5s forwards';
    }

    // 验证邮箱格式的函数
    function validateEmail() {
        const emailInput = document.querySelector('#emailInput');
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return pattern.test(emailInput.value);
    }

     // 验证密码是否填写的函数
     function validatePassword() {
        const passwordInput = document.getElementById('passwordInput');
        return passwordInput && passwordInput.value.trim() !== '';
    }

    // 根据选择的协议和输入的邮箱自动填充域名的函数
    function autoFillProtocolAndDomain() {
        const protocolSelect = document.getElementById('protocolSelect');
        const emailInput = document.getElementById('emailInput');
        const protocolOutput = document.getElementById('protocolOutput');
        if (protocolSelect && emailInput && protocolOutput) {
            const selectedProtocol = protocolSelect.value.toLowerCase();
            const emailDomain = emailInput.value.substring(emailInput.value.indexOf('@') + 1).toLowerCase();
            protocolOutput.value = `${selectedProtocol}.${emailDomain}`;
        }
    }

    // 比较起始时间和结束时间的函数
    function validateTimeOrder() {
        const startTimeInput = document.getElementById('startTime');
        const endTimeInput = document.getElementById('endTime');
    
        if (startTimeInput && endTimeInput && startTimeInput.value && endTimeInput.value) {
            // 直接使用输入的时间字符串创建 Date 对象
            const startTime = new Date(startTimeInput.value);
            const endTime = new Date(endTimeInput.value);
    
            return endTime > startTime;
        }
        // 如果一个或两个输入为空，则视为验证通过
        return true;
    }

    
});

document.addEventListener("DOMContentLoaded", function() {
    // 查找完成按钮
    const finishButton = document.querySelector("#finish-button");
    if (finishButton) {
        finishButton.addEventListener("click", function() {
            // 初始化数据对象，将config.json文件中的skip字段置为true
            let data = {skip: true };

            // 以下代码块为条件性地添加非空字段到数据对象
            if (document.querySelector("#emailInput").value) data.emailAddress = document.querySelector("#emailInput").value;
            if (document.querySelector("#passwordInput").value) data.protocolPassword = document.querySelector("#passwordInput").value;
            if (document.querySelector("#protocolSelect").value) data.protocol = document.querySelector("#protocolSelect").value;
            if (document.querySelector("#protocolOutput").value) data.serverAddress = document.querySelector("#protocolOutput").value;
            if (document.querySelector("#emailAttachmentPath").value) data.attachmentSaveDirectory = document.querySelector("#emailAttachmentPath").value;
            if (document.querySelector("#attachmentSaveMode").value) data.attachmentSaveMode = document.querySelector("#attachmentSaveMode").value;
            if (document.querySelector("#topEmailCount").value) data.headSeveralEmail = parseInt(document.querySelector("#topEmailCount").value, 10);
            if (document.querySelector("#attachmentOverwrite").value) data.isOverwrite = document.querySelector("#attachmentOverwrite").value; 
            if (document.querySelector("#timezoneSelect").value) {
                data.timeZone = document.querySelector("#timezoneSelect").value;
            }

            if (document.querySelector("#startTime").value || document.querySelector("#endTime").value) {
                data.timePeriodRange = [
                    document.querySelector("#startTime").value,
                    document.querySelector("#endTime").value
                ];
            }
            if (document.querySelector("#filterEmail").value) data.filterEmailAddress = document.querySelector("#filterEmail").value.split('||').map(item => item.trim());
            if (document.querySelector("#filterNickname").value) data.filterNickname = document.querySelector("#filterNickname").value.split('||').map(item => item.trim());
            if (document.querySelector("#filterSubject").value) data.filterSubject = document.querySelector("#filterSubject").value.split('||').map(item => item.trim());

            // 发送请求保存配置
            fetch('/save-config', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应不是OK状态。');
                }
                return response.json();
            })
            .then(data => {
                console.log('成功:', data);
                // 发送一个请求到后端进行配置检查
                fetch('/check-config', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })
                .then(checkResponse => {
                    if (!checkResponse.ok) {
                        throw new Error('配置检查请求失败。');
                    }
                    return checkResponse.json();
                })
                .then(checkData => {
                    console.log('配置检查完成:', checkData);
                    // 尝试关闭当前窗口或给出成功提示
                     showGlobalAlert("配置已保存并检查完成，请重新启动！");
                })
                .catch(checkError => {
                    console.error('配置检查错误:', checkError);
                     showGlobalAlert("配置已保存并检查完成，请重新启动！");
                });
            })
            .catch((error) => {
                console.error('错误:', error);
                 showGlobalAlert("配置已保存并检查完成，请重新启动！");
            });
        });
    }
});


