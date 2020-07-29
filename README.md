<div align="center">
<img src="static/logo.jpeg" alt="Mark Text" width="100" height="100">
<h1 align="center">MEDUSA</h1>
</div>

<div align="center">
  <strong>MEDUSA</strong><br>
    Personal Tornado Framework. Framework with log system、<br>
  <sub>babababa baba.</sub>
</div>

<div align="center">
  <h3>
    <a href="https://">
      Website
    </a>
    <span> | </span>
    <a href="https://">
      TechnologyStack
    </a>
    <span> | </span>
    <a href="https://">
      Downloads
    </a>
  </h3>
</div>

暂时记录一下需要改进的点：

1. settings.py 中用到 tornado 的 options 和 define, 需要再考量一下两种方式的优缺点

2. 需要加上用户登录以及基础的权限系统的实现

3. 装饰器路由的功能太单调，考虑是否要丰富

4. 接口参数生成和参数校验可以考虑加上自动化生成的功能

5. fast-api 考虑生成接口文档，方便测试

6. flake8 强制检查, 必须使用 typehint （是否真的强制进行类型注释 待定）

6. 加上日志模块，或许可以借鉴一下之前组长的日志系统的设计实现方式

7. 启动时自动检查数据表是否存在，不存在就创建

8. 装饰器部分优化一下，不要再每次手动 import handler 了 /importlib/pkgutil