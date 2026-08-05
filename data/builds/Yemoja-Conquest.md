---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.12
    win_rate: 0.39
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.44
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.23
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.78
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.8
  - name: Mote of Chaos
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.53
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.75
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-08-01'
  god_win_rate: 0.5167785234899329
  god_matches_won: 77
  god_matches_played: 149
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Amanita Charm, Eye of Providence,
    Gluttonous Grimoire, Oni Hunter''s Garb, Shield of the Phoenix, Freya''s Tears,
    Shifter''s Shield, Ethereal Staff, Spectral Armor, Genji''s Guard, Erosion, Mantle
    Of Discord, Soul Gem, Draconic Scale, Wish-Granting Pearl, Leviathan''s Hide,
    Jade Scepter, Yogi''s Necklace, Rod of Asclepius, Hussar''s Wings, Midgardian
    Mail, Helm of Radiance, Chandra''s Grace, Hide of the Nemean Lion, Gladiator''s
    Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Breastplate of Valor, Shield of the Phoenix, Soul Gem,
    Kinetic Cuirass, Gluttonous Grimoire, Rod of Asclepius, Eye of Providence, Chandra''s
    Grace, Oni Hunter''s Garb, Ethereal Staff, Spectral Armor, Shifter''s Shield,
    Lifebinder, Freya''s Tears, Bancroft''s Talon, Genji''s Guard, Erosion, Phoenix
    Feather, Blood-Bound Book, Draconic Scale, Wish-Granting Pearl, Jade Scepter,
    Yogi''s Necklace, Mantle Of Discord, Leviathan''s Hide, Spirit Robe.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.62
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.36
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.9
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Ethereal Staff
  - Gluttonous Grimoire
  flex_slots:
  - Oni Hunter's Garb
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Eye of Providence, Oni Hunter''s Garb, Ethereal Staff, Spear of
    the Magus, Shield of the Phoenix, Spectral Armor, Stone of Binding, Void Shield,
    Screeching Gargoyle, Genji''s Guard, Freya''s Tears, Shifter''s Shield, Mantle
    Of Discord, The Cosmic Horror, Void Stone, Erosion, Yogi''s Necklace, Draconic
    Scale, Wish-Granting Pearl, Jade Scepter, Obsidian Shard, Spear of Desolation.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.29
    Ethereal Staff:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Genji''s Guard, Oni Hunter''s Garb, Shield of the Phoenix, Freya''s
    Tears, Shifter''s Shield, Ethereal Staff, Breastplate of Valor, Spectral Armor,
    Erosion, Mantle Of Discord, Soul Gem, Draconic Scale, Wish-Granting Pearl, Leviathan''s
    Hide, Jade Scepter, Yogi''s Necklace, Rod of Asclepius, Hussar''s Wings, Midgardian
    Mail, Helm of Radiance, Chandra''s Grace, Hide of the Nemean Lion, Gladiator''s
    Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.43
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
