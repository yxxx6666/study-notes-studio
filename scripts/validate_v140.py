from pathlib import Path
root = Path(__file__).resolve().parents[1]
def read(rel): return (root/rel).read_text(encoding='utf-8', errors='ignore')
def ok(name, cond):
    if not cond: raise SystemExit(f'FAIL {name}')
    print(f'OK {name}')
required = [
 'SKILL.md','VERSION.md','CHANGELOG.md','README.md','RELEASE_REPORT.md','agents/openai.yaml',
 'handbook/clean-color-note-style.md','handbook/anti-infographic-style.md','handbook/generation-protocol.md','handbook/visual-style.md','handbook/review-rubric.md','tests/test-clean-color-note-style.md'
]
for rel in required: ok(f'{rel} exists', (root/rel).exists())
skill = read('SKILL.md')
ok('version v1.4.0', '版本：v1.4.0' in skill and 'Current version: v1.4.0' in read('VERSION.md'))
ok('clean color in skill', '清爽彩色手写笔记' in skill and 'Do not make it monochrome or overly minimal' in skill)
ok('clean color handbook', '黑色手写线条是骨架' in read('handbook/clean-color-note-style.md'))
ok('prompt color rule', 'clean colorful handwritten study-note style' in read('handbook/generation-protocol.md'))
ok('visual color rule', '黑笔骨架' in read('handbook/visual-style.md'))
ok('rubric color rule', '色彩层级检查' in read('handbook/review-rubric.md'))
ok('agent color rule', '清爽彩色手写学习笔记' in read('agents/openai.yaml'))
ok('test color rule', '清爽彩色手写笔记风' in read('tests/test-clean-color-note-style.md'))
ok('anti infographic retained', '反信息图漂移' in read('handbook/anti-infographic-style.md'))
blocked_terms = [chr(23567)+chr(40657), 'Xiao'+'hei', 'xiao'+'hei', 'black '+'creature', 'white-dot '+'eyes', chr(25220)+chr(34989)]
violations=[]
for path in root.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md','.yaml','.yml','.txt'}:
        text=path.read_text(encoding='utf-8', errors='ignore')
        for term in blocked_terms:
            if term in text:
                violations.append(str(path.relative_to(root)))
ok('sensitive reference terms clean', not violations)
print('\nAll v1.4.0 validation checks passed.')
