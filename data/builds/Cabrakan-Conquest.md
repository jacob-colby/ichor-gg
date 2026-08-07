---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.57
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.29
      win_rate: 0.59
    - name: Stampede
      pick_rate: 0.02
      win_rate: 0.56
  - name: Breastplate of Valor
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.63
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.27
    win_rate: 0.51
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.16
      win_rate: 0.61
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.52
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.59
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.52
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.55
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.38
    win_rate: 0.52
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.08
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-07'
  god_win_rate: 0.5662949194547707
  god_matches_won: 457
  god_matches_played: 807
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s Shield,
    Gluttonous Grimoire, Jotunn''s Revenge, Oni Hunter''s Garb, Freya''s Tears, The
    Crusher, Shield Splitter, Hydra''s Lament, Shield of the Phoenix, Eye of the Storm,
    Erosion, Hide of the Nemean Lion, Stampede, Draconic Scale, Spectral Armor, Pharaoh''s
    Curse, Soul Gem, Avenging Blade, Golden Blade, Yogi''s Necklace, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Mantle Of Discord, Stone of Binding, Lernaean
    Bow, Helm of Radiance, Damaru, Rod of Asclepius, Shogun''s Ofuda, Magi''s Cloak,
    Ancile, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.07
      fit: 0.67
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.48
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Eye of Providence, Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Jotunn''s
    Revenge, Oni Hunter''s Garb, The Crusher, Chandra''s Grace, Hydra''s Lament, Eye
    of the Storm, Freya''s Tears, The Reaper, Shield Splitter, Hide of the Nemean
    Lion, Erosion, Phoenix Feather, Spectral Armor, Avenging Blade, Draconic Scale,
    Golden Blade, Pharaoh''s Curse, Yogi''s Necklace, Lifebinder, Blood-Bound Book,
    Bancroft''s Talon, Leviathan''s Hide, Death Metal, Midgardian Mail, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.28
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.07
      fit: 0.66
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.54
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.56
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Berserker''s Shield, Soul Gem, Avenging Blade, Eye of Providence,
    Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle, Hydra''s Lament, Void
    Shield, Freya''s Tears, Spear of the Magus, Shield Splitter, The Reaper, Void
    Stone, The Cosmic Horror, Shield of the Phoenix, Spectral Armor, Eye of the Storm,
    Spear of Desolation, Erosion, Heartseeker, Yogi''s Necklace, Pharaoh''s Curse,
    Draconic Scale, Riptalon, Obsidian Shard, Death Metal, Golden Blade, Leviathan''s
    Hide, Silverbranch Bow, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Runeforged Hammer
  - Shifter's Shield
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Jotunn''s Revenge, Riptalon, Freya''s Tears, Lernaean Bow, Hydra''s Lament, Soul
    Gem, Shogun''s Ofuda, Shield of the Phoenix, Tyrfing, Silverbranch Bow, Spectral
    Armor, Shield Splitter, Yogi''s Necklace, Erosion, Eye of the Storm, Draconic
    Scale, Bracer of The Abyss, Dominance, Death Metal, Leviathan''s Hide, Rod of
    Asclepius, Helm of Radiance, Avenging Blade, Midgardian Mail, Bragi''s Harp, Damaru,
    Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.31
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.37
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Berserker''s Shield, Hydra''s
    Lament, Soul Gem, Gluttonous Grimoire, Eye of Providence, Oni Hunter''s Garb,
    Gladiator''s Shield, The Crusher, Chronos'' Pendant, Screeching Gargoyle, Hide
    of the Nemean Lion, Chandra''s Grace, Spear of Desolation, Spectral Armor, Erosion,
    Shield Splitter, Yogi''s Necklace, Pharaoh''s Curse, Prophetic Cloak, Draconic
    Scale, Helm of Radiance, Rod of Asclepius, Gem of Focus, Eye of the Storm, Arondight,
    Death Metal, Leviathan''s Hide, Jade Scepter, Midgardian Mail, Spear of the Magus,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.2
      fit: 0.48
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.32
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Hydra''s Lament, Oni Hunter''s Garb, Shield Splitter, Freya''s Tears, Soul Gem,
    Golden Blade, Lernaean Bow, Eye of the Storm, Pharaoh''s Curse, Shield of the
    Phoenix, Death Metal, Spectral Armor, Avenging Blade, Erosion, Yogi''s Necklace,
    The Reaper, Damaru, Draconic Scale, Spear of the Magus, Shogun''s Ofuda, Leviathan''s
    Hide, Dominance, Heartseeker, The Cosmic Horror, Helm of Radiance, Rod of Asclepius,
    Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.2
      fit: 0.23
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.44
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Amanita Charm,
    Kinetic Cuirass, The Crusher, Jotunn''s Revenge, Berserker''s Shield, Soul Gem,
    Eye of Providence, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, Freya''s
    Tears, Spear of the Magus, Shield Splitter, The Cosmic Horror, Helm of Radiance,
    Shield of the Phoenix, Rod of Asclepius, Eye of the Storm, Spectral Armor, Erosion,
    Spear of Desolation, Jade Scepter, Yogi''s Necklace, Pharaoh''s Curse, Avenging
    Blade, Draconic Scale, Golden Blade, Obsidian Shard, Lernaean Bow, The Reaper,
    Triton''s Conch, Chronos'' Pendant, Damaru, Leviathan''s Hide, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.23
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.2
      fit: 0.23
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.07
      fit: 0.52
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.29
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.5
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Oni Hunter''s Garb, Freya''s Tears,
    The Crusher, Shield Splitter, Hydra''s Lament, Shield of the Phoenix, Eye of the
    Storm, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Soul Gem, Avenging
    Blade, Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Death Metal, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Hide of the Nemean Lion, Lernaean Bow,
    Helm of Radiance, Damaru, Rod of Asclepius, Shogun''s Ofuda, Stampede, Magi''s
    Cloak, Ancile, Wyrmskin Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.27
      fit: 0.31
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.07
      fit: 0.67
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
