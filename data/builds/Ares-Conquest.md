---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.28
    win_rate: 0.59
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.73
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.57
  - name: Stampede
    pick_rate: 0.34
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.8
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.78
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.5
    - name: Spirit Robe
      pick_rate: 0.09
      win_rate: 0.5
  - name: Medallion
    pick_rate: 0.14
    win_rate: 0.75
    alternates:
    - name: Midgardian Mail
      pick_rate: 0.07
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.23
    win_rate: 0.64
  - name: Heroism
    pick_rate: 0.2
    win_rate: 0.83
  - name: Sundering Axe
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-13'
  god_win_rate: 0.6557377049180327
  god_matches_won: 40
  god_matches_played: 61
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s Shield,
    Gluttonous Grimoire, Breastplate of Valor, Shield of the Phoenix, Oni Hunter''s
    Garb, Erosion, Eye of Providence, Draconic Scale, Jotunn''s Revenge, Spectral
    Armor, Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, The Crusher, Eye of the Storm, Hydra''s Lament,
    Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak, Runeforged Hammer, Gladiator''s
    Shield, Screeching Gargoyle, Ancile, Prophetic Cloak, Xibalban Effigy, Void Shield,
    Hide of the Nemean Lion, Doublet of Binding, Rod of Asclepius, Hussar''s Wings,
    Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 0.67
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Berserker''s
    Shield, Gluttonous Grimoire, Freya''s Tears, Rod of Asclepius, Chandra''s Grace,
    Oni Hunter''s Garb, Breastplate of Valor, Erosion, Eye of Providence, Phoenix
    Feather, Draconic Scale, Jotunn''s Revenge, Spectral Armor, Pharaoh''s Curse,
    Leviathan''s Hide, Blood-Bound Book, Bancroft''s Talon, Glorious Pridwen, Runeforged
    Hammer, Lifebinder, The Crusher, Eye of the Storm, Shogun''s Ofuda, Shield Splitter,
    Riptalon, Hydra''s Lament, Gladiator''s Shield, Ancile, The Reaper, Void Shield,
    Hide of the Nemean Lion, Mantle Of Discord, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.55
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.59
      pick: 0.28
      fit: 0.65
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, Kinetic Cuirass, Soul Gem,
    The Crusher, Amanita Charm, Berserker''s Shield, Stone of Binding, Freya''s Tears,
    Screeching Gargoyle, Breastplate of Valor, Spear of the Magus, Void Shield, Oni
    Hunter''s Garb, The Cosmic Horror, Shield of the Phoenix, Void Stone, Spear of
    Desolation, Avenging Blade, Erosion, Eye of Providence, Spectral Armor, Obsidian
    Shard, Riptalon, Pharaoh''s Curse, Draconic Scale, Silverbranch Bow, Hydra''s
    Lament, The Reaper, Shield Splitter, Leviathan''s Hide, Mantle Of Discord, Runeforged
    Hammer, Helm of Radiance, Shogun''s Ofuda, Heartseeker, Eye of the Storm.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.74
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.57
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Freya''s Tears, Breastplate of Valor, Jotunn''s
    Revenge, Riptalon, The Crusher, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s
    Ofuda, Shield of the Phoenix, Hydra''s Lament, Silverbranch Bow, Tyrfing, Runeforged
    Hammer, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of
    The Abyss, Draconic Scale, Eye of the Storm, Helm of Radiance, Leviathan''s Hide,
    Mantle Of Discord, Death Metal, Stone of Binding, Eros'' Bow, Dominance, Spear
    of the Magus, Rod of Asclepius, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.36
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm,
    Gluttonous Grimoire, Berserker''s Shield, Hydra''s Lament, Oni Hunter''s Garb,
    Screeching Gargoyle, Chronos'' Pendant, The Crusher, Spear of Desolation, Chandra''s
    Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic
    Cloak, Pharaoh''s Curse, Shield Splitter, Draconic Scale, Runeforged Hammer, Helm
    of Radiance, Gem of Focus, Leviathan''s Hide, Eye of the Storm, Mantle Of Discord,
    Rod of Asclepius, Stone of Binding, Spear of the Magus, Death Metal, Arondight,
    Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Gluttonous Grimoire, Breastplate of Valor, Shield of the Phoenix,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Draconic Scale, Jotunn''s Revenge,
    Spectral Armor, Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, The Crusher, Eye of the Storm, Hydra''s Lament,
    Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak, Runeforged Hammer, Gladiator''s
    Shield, Screeching Gargoyle, Ancile, Prophetic Cloak, Xibalban Effigy, Void Shield,
    Hide of the Nemean Lion, Doublet of Binding, Rod of Asclepius, Yogi''s Necklace,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.67
  starter: *id001
---
