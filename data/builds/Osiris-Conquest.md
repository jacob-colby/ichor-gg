---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.57
    win_rate: 0.49
    alternates:
    - name: Golden Blade
      pick_rate: 0.15
      win_rate: 0.62
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Golden Blade
      pick_rate: 0.11
      win_rate: 0.46
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.6
  - name: Kinetic Cuirass
    pick_rate: 0.2
    win_rate: 0.46
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.49
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.51
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.39
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.66
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.41
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.62
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.64
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.62
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.42
    win_rate: 0.59
  - name: Death's Toll
    pick_rate: 0.27
    win_rate: 0.37
  - name: Sundering Axe
    pick_rate: 0.09
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-09'
  god_win_rate: 0.4928571428571429
  god_matches_won: 207
  god_matches_played: 420
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-09'
  god_matches_analyzed: 15881
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, The Crusher, Runeforged Hammer, Jotunn''s
    Revenge, Lernaean Bow, Genji''s Guard, Eye of Providence, Pharaoh''s Curse, Oni
    Hunter''s Garb, Hydra''s Lament, Damaru, Shogun''s Ofuda, Eye of the Storm, Avenging
    Blade, Yogi''s Necklace, Shield Splitter, Breastplate of Valor, Dominance, Spectral
    Armor, Shield of the Phoenix, Tyrfing, Freya''s Tears, Erosion, Leviathan''s Hide,
    Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.55
      win: 0.62
      pick: 0.15
      fit: 0.57
    Berserker's Shield:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.33
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.5
      efficiency: 0.54
      win: 0.61
      pick: 0.08
      fit: 0.25
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Shield of the Phoenix, Eye of Providence,
    Runeforged Hammer, Genji''s Guard, The Crusher, Oni Hunter''s Garb, Pharaoh''s
    Curse, Riptalon, Jotunn''s Revenge, The Reaper, Lernaean Bow, Chandra''s Grace,
    Hydra''s Lament, Shogun''s Ofuda, Damaru, Eye of the Storm, Shield Splitter, Breastplate
    of Valor, Phoenix Feather, Spectral Armor, Yogi''s Necklace, Freya''s Tears, Avenging
    Blade, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.15
      fit: 0.53
    Berserker's Shield:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.33
      fit: 0.47
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.46
      pick: 0.2
      fit: 0.54
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.63
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.54
      win: 0.61
      pick: 0.08
      fit: 0.3
    Amanita Charm:
      total: 0.57
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Golden Blade, The Crusher, Jotunn''s Revenge, Avenging Blade, Amanita
    Charm, Runeforged Hammer, Genji''s Guard, Riptalon, Oni Hunter''s Garb, Eye of
    Providence, Lernaean Bow, Hydra''s Lament, The Reaper, Silverbranch Bow, Pharaoh''s
    Curse, Void Shield, Tekko-Kagi, Damaru, Stone of Binding, Screeching Gargoyle,
    Heartseeker, Breastplate of Valor, Yogi''s Necklace, Void Stone, Shogun''s Ofuda,
    Spectral Armor, Eye of the Storm.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.15
      fit: 0.42
    Avenging Blade:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.33
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Hide of the Nemean Lion
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Genji''s Guard, Riptalon, The Crusher,
    Pharaoh''s Curse, Lernaean Bow, Runeforged Hammer, Oni Hunter''s Garb, Eye of
    Providence, Jotunn''s Revenge, Tyrfing, Shogun''s Ofuda, Silverbranch Bow, Hydra''s
    Lament, Breastplate of Valor, Yogi''s Necklace, Damaru, Dominance, Spectral Armor,
    Shield of the Phoenix, Freya''s Tears, Avenging Blade, Eros'' Bow, Eye of the
    Storm, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.55
      win: 0.62
      pick: 0.15
      fit: 0.6
    Genji's Guard:
      total: 0.49
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.33
      fit: 0.41
    Hide of the Nemean Lion:
      total: 0.49
      efficiency: 0.54
      win: 0.61
      pick: 0.08
      fit: 0.19
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Golden Blade, Genji''s Guard, Jotunn''s
    Revenge, Hydra''s Lament, Breastplate of Valor, Shield of the Phoenix, Amanita
    Charm, Freya''s Tears, The Crusher, Oni Hunter''s Garb, Eye of Providence, Runeforged
    Hammer, Pharaoh''s Curse, Chandra''s Grace, Lernaean Bow, Yogi''s Necklace, Screeching
    Gargoyle, Shogun''s Ofuda, Damaru, Spectral Armor, Arondight, Gladiator''s Shield,
    Avenging Blade, Eye of the Storm, Leviathan''s Hide, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.55
      win: 0.62
      pick: 0.15
      fit: 0.34
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.33
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, The Crusher, Runeforged Hammer, Golden
    Blade, Jotunn''s Revenge, Lernaean Bow, Genji''s Guard, Eye of Providence, Pharaoh''s
    Curse, Oni Hunter''s Garb, Hydra''s Lament, Damaru, Eye of the Storm, Shogun''s
    Ofuda, Avenging Blade, Yogi''s Necklace, Shield Splitter, Breastplate of Valor,
    Dominance, Spectral Armor, Shield of the Phoenix, Tyrfing, Freya''s Tears, Erosion,
    Leviathan''s Hide, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.55
      win: 0.62
      pick: 0.15
      fit: 0.57
    Berserker's Shield:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.33
      fit: 0.45
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.6
      win: 0.46
      pick: 0.2
      fit: 0.45
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
---
