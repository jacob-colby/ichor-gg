---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.46
  aspect_win_rate: 0.54
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.49
    win_rate: 0.55
    alternates:
    - name: Tyrfing
      pick_rate: 0.27
      win_rate: 0.57
    - name: The Reaper
      pick_rate: 0.04
      win_rate: 0.5
  - name: Dagger of Frenzy
    pick_rate: 0.34
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.68
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.17
    win_rate: 0.48
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.63
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.43
  - name: Dominance
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Riptalon
      pick_rate: 0.21
      win_rate: 0.53
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.05
    win_rate: 0.54
    alternates:
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.68
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.61
  - name: Manchu Bow
    pick_rate: 0.08
    win_rate: 0.42
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.55
    - name: Riptalon
      pick_rate: 0.06
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-08-01'
  god_win_rate: 0.5460750853242321
  god_matches_won: 160
  god_matches_played: 293
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Dominance
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher, Dominance,
    Death Metal, Berserker''s Shield, Genji''s Guard, Lernaean Bow, Hydra''s Lament,
    Damaru, Spear of the Magus, Bragi''s Harp, Bracer of The Abyss, Runeforged Hammer,
    The Cosmic Horror, Golden Blade, The Reaper, Breastplate of Valor, Silverbranch
    Bow, Spear of Desolation, Blood-Bound Book, Bancroft''s Talon, Tekko-Kagi, Nimble
    Ring, Pharaoh''s Curse, Obsidian Shard, Amanita Charm, Chronos'' Pendant, Rod
    of Asclepius, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Helm of Radiance,
    Jade Scepter, Heartseeker, Demon Blade, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.51
      efficiency: 0.53
      win: 0.59
      pick: 0.11
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Damaru
  - Demon Blade
  - The Crusher
  flex_slots:
  - Damaru
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Death Metal, Jotunn''s Revenge, The Crusher,
    Dominance, Berserker''s Shield, Genji''s Guard, Damaru, Hydra''s Lament, Lernaean
    Bow, Spear of the Magus, The Cosmic Horror, Bracer of The Abyss, Bragi''s Harp,
    Runeforged Hammer, Breastplate of Valor, The Reaper, Golden Blade, Spear of Desolation,
    Silverbranch Bow, Blood-Bound Book, Bancroft''s Talon, Obsidian Shard, Nimble
    Ring, Amanita Charm, Chronos'' Pendant, Pharaoh''s Curse, Rod of Asclepius, Tekko-Kagi,
    Oni Hunter''s Garb, Yogi''s Necklace, Helm of Radiance, Kinetic Cuirass, Jade
    Scepter, Freya''s Tears, Demon Blade, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Damaru:
      total: 0.49
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.36
    Demon Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Dominance
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher, Dominance,
    Death Metal, Berserker''s Shield, Genji''s Guard, Hydra''s Lament, Spear of the
    Magus, Lernaean Bow, Damaru, The Cosmic Horror, Spear of Desolation, Breastplate
    of Valor, The Reaper, Runeforged Hammer, Silverbranch Bow, Bracer of The Abyss,
    Bragi''s Harp, Golden Blade, Obsidian Shard, Chronos'' Pendant, Tekko-Kagi, Blood-Bound
    Book, Bancroft''s Talon, Amanita Charm, Oni Hunter''s Garb, Pharaoh''s Curse,
    Rod of Asclepius, Yogi''s Necklace, Kinetic Cuirass, Heartseeker, Freya''s Tears,
    Nimble Ring, Helm of Radiance, Dreamer''s Idol, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    Dominance:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.11
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.0
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - The Crusher
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Soul Gem, Gluttonous Grimoire, Berserker''s
    Shield, Rod of Asclepius, Shield of the Phoenix, The Reaper, Genji''s Guard, Blood-Bound
    Book, The Crusher, Bancroft''s Talon, Jotunn''s Revenge, Kinetic Cuirass, Death
    Metal, Eye of Providence, Oni Hunter''s Garb, Runeforged Hammer, Chandra''s Grace,
    Pharaoh''s Curse, Hydra''s Lament, Breastplate of Valor, Lifebinder, Golden Blade,
    Lernaean Bow, Damaru, Yogi''s Necklace, Spear of the Magus, Freya''s Tears, Phoenix
    Feather, Spectral Armor, Shogun''s Ofuda, The Cosmic Horror, Bracer of The Abyss,
    Helm of Radiance, Jade Scepter, Shield Splitter, Umbral Link, Eye of the Storm.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.29
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Dominance
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Dominance
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Soul Gem, Jotunn''s Revenge, Dominance,
    Berserker''s Shield, Death Metal, Spear of the Magus, The Cosmic Horror, Genji''s
    Guard, Avenging Blade, The Reaper, Hydra''s Lament, Lernaean Bow, Silverbranch
    Bow, Damaru, Spear of Desolation, Obsidian Shard, Tekko-Kagi, Runeforged Hammer,
    Bracer of The Abyss, Screeching Gargoyle, Breastplate of Valor, Golden Blade,
    Bragi''s Harp, Heartseeker, Blood-Bound Book, Amanita Charm, Bancroft''s Talon,
    Dreamer''s Idol, The World Stone, Oni Hunter''s Garb, Doom Orb, Pharaoh''s Curse,
    Stone of Binding, Yogi''s Necklace, Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Dominance:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.11
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.0
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Gluttonous Grimoire
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Dominance
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Dominance, Berserker''s Shield, The Crusher,
    Jotunn''s Revenge, Death Metal, Genji''s Guard, Golden Blade, Silverbranch Bow,
    Lernaean Bow, Hydra''s Lament, Damaru, Spear of the Magus, Bracer of The Abyss,
    The Cosmic Horror, Runeforged Hammer, Bragi''s Harp, Breastplate of Valor, The
    Reaper, Blood-Bound Book, Spear of Desolation, Pharaoh''s Curse, Bancroft''s Talon,
    Amanita Charm, Oni Hunter''s Garb, Nimble Ring, Rod of Asclepius, Yogi''s Necklace,
    Chronos'' Pendant, Obsidian Shard, Kinetic Cuirass, Tekko-Kagi, Helm of Radiance,
    Jade Scepter, Eye of Providence, Toxic Blade, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.2
    Tyrfing:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.27
      fit: 0.54
    Dominance:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.11
      fit: 0.31
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.0
    Soul Gem:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Genji''s
    Guard, Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher,
    Dominance, Breastplate of Valor, Death Metal, Spear of Desolation, Chronos'' Pendant,
    Lernaean Bow, Damaru, Freya''s Tears, Spear of the Magus, Shield of the Phoenix,
    Runeforged Hammer, Bracer of The Abyss, The Cosmic Horror, Silverbranch Bow, Golden
    Blade, Gem of Focus, Amanita Charm, The Reaper, Arondight, Pharaoh''s Curse, Oni
    Hunter''s Garb, Screeching Gargoyle, Chandra''s Grace, Blood-Bound Book, Bragi''s
    Harp, Yogi''s Necklace, Kinetic Cuirass, Bancroft''s Talon, Pendulum Blade, Obsidian
    Shard, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.0
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The
    Crusher, Death Metal, Berserker''s Shield, Genji''s Guard, Lernaean Bow, Hydra''s
    Lament, Damaru, Spear of the Magus, Bragi''s Harp, Bracer of The Abyss, Runeforged
    Hammer, The Cosmic Horror, Golden Blade, The Reaper, Breastplate of Valor, Silverbranch
    Bow, Spear of Desolation, Dominance, Blood-Bound Book, Bancroft''s Talon, Tekko-Kagi,
    Nimble Ring, Pharaoh''s Curse, Obsidian Shard, Amanita Charm, Chronos'' Pendant,
    Rod of Asclepius, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Helm
    of Radiance, Jade Scepter, Heartseeker, Demon Blade, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Death
    Metal, The Reaper, Berserker''s Shield, Amanita Charm, Blood-Bound Book, Dominance,
    Rod of Asclepius, Bancroft''s Talon, Genji''s Guard, Hydra''s Lament, Runeforged
    Hammer, Damaru, Shield of the Phoenix, Spear of the Magus, Lernaean Bow, Golden
    Blade, The Cosmic Horror, Oni Hunter''s Garb, Chandra''s Grace, Breastplate of
    Valor, Yogi''s Necklace, Kinetic Cuirass, Spear of Desolation, Lifebinder, Bracer
    of The Abyss, Bragi''s Harp, Jade Scepter, Pharaoh''s Curse, Eye of Providence,
    Avenging Blade, Obsidian Shard, Chronos'' Pendant, Bloodforge, Silverbranch Bow,
    Nimble Ring.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.09
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Berserker's Shield
  - Death Metal
  - Shifter's Shield
  - Damaru
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Damaru
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Death Metal, Amanita Charm, Dominance, The Reaper, Blood-Bound Book,
    Rod of Asclepius, Bancroft''s Talon, Genji''s Guard, Damaru, Hydra''s Lament,
    Runeforged Hammer, Shield of the Phoenix, Lernaean Bow, Spear of the Magus, Golden
    Blade, The Cosmic Horror, Bracer of The Abyss, Oni Hunter''s Garb, Breastplate
    of Valor, Chandra''s Grace, Pharaoh''s Curse, Yogi''s Necklace, Kinetic Cuirass,
    Bragi''s Harp, Lifebinder, Spear of Desolation, Silverbranch Bow, Jade Scepter,
    Nimble Ring, Eye of Providence, Obsidian Shard, Chronos'' Pendant, Avenging Blade,
    Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.08
    Damaru:
      total: 0.48
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.31
    Demon Blade:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.48
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Shifter's Shield
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, The Reaper,
    Berserker''s Shield, Amanita Charm, Death Metal, Genji''s Guard, Blood-Bound Book,
    Rod of Asclepius, Bancroft''s Talon, Hydra''s Lament, Shield of the Phoenix, Spear
    of the Magus, Runeforged Hammer, Damaru, The Cosmic Horror, Spear of Desolation,
    Breastplate of Valor, Chandra''s Grace, Lernaean Bow, Oni Hunter''s Garb, Golden
    Blade, Yogi''s Necklace, Kinetic Cuirass, Obsidian Shard, Chronos'' Pendant, Lifebinder,
    Silverbranch Bow, Bracer of The Abyss, Jade Scepter, Eye of Providence, Pharaoh''s
    Curse, Bragi''s Harp, Avenging Blade, Freya''s Tears, Heartseeker, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.08
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - The Crusher
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Soul Gem, Amanita Charm, Gluttonous Grimoire, Berserker''s
    Shield, Rod of Asclepius, Shield of the Phoenix, The Reaper, Blood-Bound Book,
    Bancroft''s Talon, The Crusher, Genji''s Guard, Jotunn''s Revenge, Kinetic Cuirass,
    Death Metal, Eye of Providence, Oni Hunter''s Garb, Runeforged Hammer, Chandra''s
    Grace, Hydra''s Lament, Breastplate of Valor, Lifebinder, Damaru, Pharaoh''s Curse,
    Yogi''s Necklace, Spear of the Magus, Freya''s Tears, Golden Blade, Lernaean Bow,
    Phoenix Feather, Spectral Armor, The Cosmic Horror, Umbral Link, Bloodforge, Helm
    of Radiance, Jade Scepter, Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.29
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.29
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, The
    Reaper, Berserker''s Shield, Amanita Charm, Avenging Blade, Death Metal, Blood-Bound
    Book, Rod of Asclepius, Spear of the Magus, Bancroft''s Talon, Genji''s Guard,
    The Cosmic Horror, Hydra''s Lament, Runeforged Hammer, Shield of the Phoenix,
    Damaru, Spear of Desolation, Obsidian Shard, Lernaean Bow, Silverbranch Bow, Screeching
    Gargoyle, Oni Hunter''s Garb, Golden Blade, Breastplate of Valor, Yogi''s Necklace,
    Chandra''s Grace, Kinetic Cuirass, Void Shield, Heartseeker, Tekko-Kagi, Lifebinder,
    Bracer of The Abyss, Jade Scepter, Eye of Providence, Pharaoh''s Curse, Stone
    of Binding.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.08
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Shifter's Shield
  - Riptalon
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Dominance
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Berserker''s Shield, Dominance, The Crusher,
    Amanita Charm, Jotunn''s Revenge, Rod of Asclepius, Golden Blade, Death Metal,
    Genji''s Guard, Blood-Bound Book, The Reaper, Bancroft''s Talon, Silverbranch
    Bow, Lernaean Bow, Hydra''s Lament, Shield of the Phoenix, Runeforged Hammer,
    Damaru, Spear of the Magus, Bracer of The Abyss, Pharaoh''s Curse, Oni Hunter''s
    Garb, Breastplate of Valor, The Cosmic Horror, Yogi''s Necklace, Chandra''s Grace,
    Kinetic Cuirass, Bragi''s Harp, Lifebinder, Spear of Desolation, Jade Scepter,
    Eye of Providence, Nimble Ring, Chronos'' Pendant, Shogun''s Ofuda, Obsidian Shard.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Tyrfing:
      total: 0.51
      efficiency: 0.47
      win: 0.57
      pick: 0.27
      fit: 0.51
    Dominance:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.11
      fit: 0.28
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.07
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.48
      pick: 0.17
      fit: 0.69
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, Jotunn''s
    Revenge, Genji''s Guard, Shield of the Phoenix, Hydra''s Lament, Berserker''s
    Shield, Amanita Charm, The Crusher, Breastplate of Valor, Chandra''s Grace, The
    Reaper, Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Death Metal, Spear
    of Desolation, Runeforged Hammer, Chronos'' Pendant, Damaru, Freya''s Tears, Spear
    of the Magus, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Lernaean
    Bow, The Cosmic Horror, Golden Blade, Pharaoh''s Curse, Gem of Focus, Eye of Providence,
    Arondight, Lifebinder, Screeching Gargoyle, Bracer of The Abyss, Jade Scepter,
    Silverbranch Bow, Spectral Armor, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.26
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Hydra's Lament:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.68
      pick: 0.09
      fit: 0.08
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Gluttonous Grimoire, The Crusher, Jotunn''s
    Revenge, Death Metal, Berserker''s Shield, The Reaper, Amanita Charm, Blood-Bound
    Book, Rod of Asclepius, Bancroft''s Talon, Genji''s Guard, Hydra''s Lament, Runeforged
    Hammer, Damaru, Shield of the Phoenix, Spear of the Magus, Lernaean Bow, Golden
    Blade, The Cosmic Horror, Oni Hunter''s Garb, Chandra''s Grace, Breastplate of
    Valor, Yogi''s Necklace, Kinetic Cuirass, Spear of Desolation, Lifebinder, Bracer
    of The Abyss, Bragi''s Harp, Jade Scepter, Pharaoh''s Curse, Eye of Providence,
    Avenging Blade, Obsidian Shard, Chronos'' Pendant, Bloodforge, Silverbranch Bow,
    Dominance, Nimble Ring.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
---
