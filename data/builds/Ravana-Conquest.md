---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.43
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.47
    - name: Barbed Carver
      pick_rate: 0.07
      win_rate: 0.4
  - name: Barbed Carver
    pick_rate: 0.14
    win_rate: 0.47
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.42
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.51
  - name: The Reaper
    pick_rate: 0.12
    win_rate: 0.54
    alternates:
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.43
  - name: Heartseeker
    pick_rate: 0.23
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.33
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.41
  - name: Titan's Bane
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.55
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.29
  - name: Skeggox
    pick_rate: 0.06
    win_rate: 0.21
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.05
      win_rate: 0.62
    - name: Axe
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.51
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.37
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-08-29'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter,
    Eye of the Storm, Breastplate of Valor, Berserker''s Shield, Avenging Blade, Shield
    of the Phoenix, Hydra''s Lament, The Crusher, Erosion, Eye of Providence, Draconic
    Scale, Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade,
    Screeching Gargoyle, Stone of Binding, Hide of the Nemean Lion, Genji''s Guard,
    Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.58
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.27
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.47
      pick: 0.38
      fit: 0.65
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.55
    Avatar's Parashu:
      total: 0.51
      efficiency: 0.45
      win: 0.62
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.42
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Breastplate of Valor, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Avenging Blade, The Crusher,
    Shield of the Phoenix, Transcendence, Daybreak Gavel, Arondight, Screeching Gargoyle,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Draconic Scale,
    Pendulum Blade, Midgardian Mail, Hide of the Nemean Lion, Genji''s Guard, Freya''s
    Tears.'
  slot_scores:
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.52
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.47
      pick: 0.38
      fit: 0.62
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.44
    Avatar's Parashu:
      total: 0.5
      efficiency: 0.45
      win: 0.62
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Breastplate of Valor, Runeforged Hammer, Kinetic Cuirass,
    Berserker''s Shield, Shield of the Phoenix, Shield Splitter, The Crusher, Hydra''s
    Lament, Eye of the Storm, Pendulum Blade, Avenging Blade, Screeching Gargoyle,
    Daybreak Gavel, Arondight, Erosion, Eye of Providence, Draconic Scale, Stone of
    Binding, Midgardian Mail, Hide of the Nemean Lion, Leviathan''s Hide, Genji''s
    Guard, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.56
    Transcendence:
      total: 0.42
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.16
    The Reaper:
      total: 0.49
      efficiency: 0.5
      win: 0.54
      pick: 0.19
      fit: 0.4
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.47
      pick: 0.38
      fit: 0.6
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.5
    Avatar's Parashu:
      total: 0.5
      efficiency: 0.45
      win: 0.62
      pick: 0.15
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Avatar's Parashu
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer,
    Shield Splitter, Breastplate of Valor, Eye of the Storm, Berserker''s Shield,
    Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix Feather,
    Avenging Blade, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Hydra''s Lament, Daybreak Gavel, The Crusher, Hide of the Nemean Lion, Magi''s
    Cloak, Genji''s Guard, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.49
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.61
    The Reaper:
      total: 0.53
      efficiency: 0.5
      win: 0.54
      pick: 0.19
      fit: 0.68
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.48
    Avatar's Parashu:
      total: 0.5
      efficiency: 0.45
      win: 0.62
      pick: 0.15
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Amanita Charm, Screeching Gargoyle, Runeforged Hammer,
    Stone of Binding, The Crusher, Kinetic Cuirass, Void Shield, Breastplate of Valor,
    Void Stone, Shield Splitter, Pendulum Blade, Eye of the Storm, Berserker''s Shield,
    Shield of the Phoenix, Hydra''s Lament, Daybreak Gavel, Tekko-Kagi, Erosion, Eye
    of Providence, Draconic Scale, Arondight, Genji''s Guard, Freya''s Tears.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.47
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.67
    The Reaper:
      total: 0.51
      efficiency: 0.5
      win: 0.54
      pick: 0.19
      fit: 0.57
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.47
      pick: 0.38
      fit: 0.77
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.67
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.45
      win: 0.62
      pick: 0.15
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Titan's Bane
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon, Tyrfing,
    Silverbranch Bow, Kinetic Cuirass, Breastplate of Valor, Toxic Blade, Runeforged
    Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shield Splitter,
    Eye of the Storm, Shield of the Phoenix, Daybreak Gavel, Avenging Blade, Dominance,
    Erosion, Hydra''s Lament, Eye of Providence, Screeching Gargoyle, Genji''s Guard,
    Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.31
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.54
      pick: 0.19
      fit: 0.3
    Riptalon:
      total: 0.47
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.55
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Shield of the Phoenix, Kinetic Cuirass, Screeching Gargoyle, Hydra''s Lament,
    Runeforged Hammer, Berserker''s Shield, Arondight, Gladiator''s Shield, Eye of
    Erebus, Pendulum Blade, Genji''s Guard, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence, Avenging
    Blade, Draconic Scale, Midgardian Mail, Stone of Binding, Freya''s Tears, The
    Crusher.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.59
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.41
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.57
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.63
      pick: 0.15
      fit: 0.34
    Avatar's Parashu:
      total: 0.48
      efficiency: 0.45
      win: 0.62
      pick: 0.15
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Freya''s
    Tears, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor,
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, The
    Crusher, Erosion, Eye of Providence, Draconic Scale, Daybreak Gavel, Pendulum
    Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of
    Binding, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.42
      pick: 0.38
      fit: 0.58
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.48
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.57
      win: 0.47
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.4
      efficiency: 0.61
      win: 0.29
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.42
  starter: *id001
---
